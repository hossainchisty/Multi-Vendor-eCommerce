from django.test import TestCase
from review.models import Review


class TestReviewModel(TestCase):
    '''
    Test suite for review modules.
    '''

    def setUp(self):
        '''
        Set up test data for the review model.
        '''
        Review.objects.create(
            feedback='Test review',
            riderReview='Test review content',
        )

    def tearDown(self):
        '''
        Clean up test data for the review model.
        '''
        Review.objects.all().delete()

    def test_review_feedback(self):
        '''
        Test review model for feedback.
        '''
        review = Review.objects.get(feedback='Test review')
        self.assertEqual(review.feedback, 'Test review')

    def test_review_rider_review(self):
        '''
        Test review model for rider review.
        '''
        review = Review.objects.get(riderReview='Test review content')
        self.assertEqual(review.riderReview, 'Test review content')

    def test_review_verbose_name_plural(self):
        '''
        Test review model for verbose name plural.
        '''
        self.assertEqual(str(Review._meta.verbose_name_plural), 'Customer feedback')
