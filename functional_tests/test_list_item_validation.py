from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # User goes to homepage and enters empty list item

        # Page refreshes with error message

        # Tries again with text

        # Enters second blank item

        # Similar error occurs

        # Corrects by inputing some text
        self.fail('write me!')
