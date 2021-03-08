# Stdlib imports
import os
from enum import Enum

# Library imports
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

class SentimentType(Enum):
    """ Class | Sentiment Type

    An enum containing possible types of sentiments.
    """
    negative = "negative"
    neutral  = "neutral"
    positive = "positive"

class SentimentResult:
    """ Class | Sentiment Result

    This class holds information on the original text of a sentiment input,
    and the polarity score the text was given.

    Parameters
    ----------
    text: :class:`str`
        A string containing the original input text that was evaluated.
    negative: :class:`float`
        The negativity score for the input text, on a scale of -1 to 1.
    neutral: :class:`float`
        The neutrality score for the input text, on a scale of -1 to 1.
    positive: :class:`float`
        The positivity score for the input text, on a scale of -1 to 1.
    compound: :class:`float`
        The compound positivity score for the input text.
    ploarity: :class: `float`
        The polarity score for the inpu text.
    """
    def __init__(self, text, negative, neutral, positive, compound, polarity):
        self.text = text
        self.negativity_score = negative
        self.neutrality_score = neutral
        self.positivity_score = positive
        self.compound_score = compound
        self.polarity_score = polarity

    @property
    def sentiment(self):
        """ :class:`.SentimentType`: Returns an enum representing the overall sentiment of the text. """
        if self.negativity_score > self.positivity_score:
            return SentimentType('negative')
        elif self.negativity_score < self.positivity_score:
            return SentimentType('positive')
        else:
            return SentimentType('neutral')

class Sentiment:
    """ Class | Sentiment

    This class utilizes the Natural Language Toolkit to observe the contents
    of a list of provided texts, and sort them into positive, negative,
    and neutral sentiments.

    Parameters
    ----------
    inputs: :class:`list`[:class:`str`]
        A list of strings to be analyzed for sentiment values.

    Attributes
    ----------
    polarity: :class:`int`
        The overall sentiment value of the provided inputs.
    neutral_list: :class:`list`[:class:`.SentimentResult`]
        A list of all neutral valued inputss, and their scores.
    positive_list: :class:`list`[:class:`.SentimentResult`]
        A list of all positive valued inputs, and their scores.
    negative_list: :class:`list`[:class:`.SentimentResult`]
        A list of all negative valued inputs, and their scores.
    """
    def __init__(self, inputs):
        self.inputs = inputs

        self.polarity = 0
        self.neutral_list = []
        self.positive_list = []
        self.negative_list = []

        self.process_sentiments()

        self.print_results()

    @property
    def neutral_count(self):
        """ :class:`int`: The count of neutrally scored inputs. """
        return len(self.neutral_list)

    @property
    def positive_count(self):
        """ :class:`int`: The count of positively scored inputs. """
        return len(self.positive_list)

    @property
    def negative_count(self):
        """ :class:`int`: The count of negatively scored inputs. """
        return len(self.negative_list)

    @property
    def positive_percent(self):
        """ :class:`float`: The percentage of positive entries vs total. """
        return self.percentage(self.positive_count, len(self.inputs))

    @property
    def neutral_percent(self):
        """ :class:`float`: The percentage of neutral entries vs total. """
        return self.percentage(self.neutral_count, len(self.inputs))

    @property
    def negative_percent(self):
        """ :class:`float`: The percentage of negative entries vs total. """
        return self.percentage(self.negative_count, len(self.inputs))

    @staticmethod
    def percentage(part, whole):
        """ :class:`float`: The calculated percentage based on inputs.

        Parameters
        ----------
        part: :class:`float` | :class:`int
            The smaller part of the total number to count the percentage of.
        whole: :class:`float` | :class:`int`
            The total number of entries that the part is a percentage of.
        """
        return (float(part)/float(whole)) * 100

    def process_sentiments(self,):
        """ Method | Process Sentiments

        This method handles finding scores and assigning the input texts
        to categories or negative, positive, or neutral.
        """
        for input in self.inputs:
            # Scoring the input text
            blob = TextBlob(input)
            score = SentimentIntensityAnalyzer().polarity_scores(input)

            # Processing the scoring of the text
            self.polarity += blob.sentiment.polarity

            result = SentimentResult(
                input,
                score['neg'],
                score['neu'],
                score['pos'],
                score['compound'],
                blob.sentiment.polarity
            )

            if result.sentiment == SentimentType.negative:
                self.negative_list.append(result)
            elif result.sentiment == SentimentType.positive:
                self.positive_list.append(result)
            elif result.sentiment == SentimentType.neutral:
                self.neutral_list.append(result)

    def print_results(self):
        """ Method | Print Results

        Prints the results of determining the sentiment scores of inputs.
        """
        num_inputs = len(self.inputs)
        positive = round(self.positive_percent, 1)
        neutral = round(self.neutral_percent, 1)
        negative = round(self.negative_percent, 1)

        print(f"Positive: {self.positive_count} ({positive}%)")
        print(f"Neutral: {self.neutral_count} ({neutral}%)")
        print(f"Negative: {self.negative_count} ({negative}%)")
        print(f"Polarity: {self.polarity}")
