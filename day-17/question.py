class Question:
    def __init__(self, question_text: str, answer: str) -> None:
        """
        Initializes a Question object with the provided question_text and answer values.

        Args:
            question_text (str): The text of the question.
            answer (Any): The answer to the question.

        Returns:
            None
        """
        self.text = question_text
        self.ans = answer