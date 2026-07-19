from app.agents.reviewer import reviewer
from app.services.logger_service import logger


class RetryManager:
    """
    Retry Manager

    Responsibilities
    ----------------
    • Review analysis quality.
    • Decide whether to retry.
    • Stop after max retries.
    """

    MIN_SCORE = 7.0

    def should_retry(
        self,
        state,
    ) -> bool:

        logger.info("Reviewing analysis...")

        review = reviewer.run(
            state.analysis,
            state.summary,
            state.insights,
        )

        state.review = review.model_dump()

        state.review_score = review.score

        if (
            review.score < self.MIN_SCORE
            and state.retry_count < state.max_retries
        ):

            state.retry_count += 1

            logger.warning(
                f"Retry {state.retry_count}/{state.max_retries}"
            )

            return True

        logger.info("Retry not required.")

        return False

    def reset(self, state):

        logger.info("Resetting retry manager.")

        state.retry_count = 0

        state.review_score = 0.0

        return state

    def maximum_retries_reached(
        self,
        state,
    ) -> bool:

        return state.retry_count >= state.max_retries


retry_manager = RetryManager()