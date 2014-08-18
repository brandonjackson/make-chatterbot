"""
Modified version of aiml.Kernel.

Overview of changes:
- public matchedPattern() method added that makes it possible to
  see the underlying pattern match that dictates the bot's response
"""

import aiml
import string
import re
import pprint

class MyKernel(aiml.Kernel):

    def matchedPattern(self, input, sessionID='_global'):
        """
        Modified version of aiml.Kernel._respond(). Instead of using the
        matches to generate a response, now it returns the pattern that
        matches the input as well as the matching template.

        @todo make sure sessionID is still working correctly
        """

        if len(input) == 0:
            return ""

        # if sessionID is 0:
        #     print self._sessions
        #     print self.getSessionData()

        # guard against infinite recursion
        inputStack = self.getPredicate(self._inputStack, sessionID)
        if len(inputStack) > self._maxRecursionDepth:
            if self._verboseMode:
                err = "WARNING: maximum recursion depth exceeded (input='%s')" % input.encode(self._textEncoding, 'replace')
                sys.stderr.write(err)
            return ""

        # # push the input onto the input stack
        # inputStack = self.getPredicate(self._inputStack, sessionID)
        # inputStack.append(input)
        # self.setPredicate(self._inputStack, inputStack, sessionID)

        # run the input through the 'normal' subber
        subbedInput = self._subbers['normal'].sub(input)

        # fetch the bot's previous response, to pass to the match()
        # function as 'that'.
        outputHistory = self.getPredicate(self._outputHistory, sessionID)
        try: that = outputHistory[-1]
        except IndexError: that = ""
        subbedThat = self._subbers['normal'].sub(that)

        # fetch the current topic
        topic = self.getPredicate("topic", sessionID)
        subbedTopic = self._subbers['normal'].sub(topic)

        # Determine the final response.
        response = ""
        # elem = self._brain.match(subbedInput, subbedThat, subbedTopic)
        match, template = self._pattern(subbedInput, subbedThat, subbedTopic)

        return match, template


    def _pattern(self, pattern, that, topic):
        """
        Modified version of aiml.PatternMgr._match(). Now returns the pattern that
        matches the input as well as the matching template.
        """

        if len(pattern) == 0:
            return None
        # Mutilate the input.  Remove all punctuation and convert the
        # text to all caps.
        input = string.upper(pattern)
        input = re.sub(self._brain._puncStripRE, " ", input)
        if that.strip() == u"": that = u"ULTRABOGUSDUMMYTHAT" # 'that' must never be empty
        thatInput = string.upper(that)
        thatInput = re.sub(self._brain._puncStripRE, " ", thatInput)
        thatInput = re.sub(self._brain._whitespaceRE, " ", thatInput)
        if topic.strip() == u"": topic = u"ULTRABOGUSDUMMYTOPIC" # 'topic' must never be empty
        topicInput = string.upper(topic)
        topicInput = re.sub(self._brain._puncStripRE, " ", topicInput)
        

        # Pass the input off to the recursive call
        patMatch, template = self._brain._match(input.split(), thatInput.split(), topicInput.split(), self._brain._root)

        return patMatch, template

    @staticmethod
    def formatMatchedPattern(match):
        """formats pattern list into a usable string"""

        # Replace all 1's with Wildcard Asterisks
        match = [str(m) for m in match] # convert all to strings
        match = [m.replace('1',"*") for m in match]

        # The list needs to be broken into three chunks corresponding to the 
        # three types of matching patterns
        matchParts = MyKernel.partition(match,[match.index('3'), match.index('4')])
        matchedInput = matchParts[0]
        matchedThat = matchParts[1]
        del matchedThat[0]
        matchedTopic = matchParts[2]
        del matchedTopic[0]

        inputStr = " ".join(matchedInput)
        thatStr = " ".join(matchedThat)
        topicStr = " ".join(matchedTopic)

        matchStr = ""
        if inputStr != '0':
            matchStr += inputStr
        elif thatStr != "*":
            matchStr += thatStr + " (match from previous conversation)"
        elif topicStr != "*":
            topicStr += topicStr + " (match from topic)"

        return matchStr


    @staticmethod
    def partition(alist, indices):
        """partitions a list into chunks at the given indices"""
        return [alist[i:j] for i, j in zip([0]+indices, indices+[None])]
