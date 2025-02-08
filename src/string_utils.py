"""String utils."""
# src/string_utils.py


class StringUtils:
    """String Utils module."""

    def reverse_string(self, text: str) -> str:
        """Reverse a string."""
        return text[::-1]

    def count_words(self, text: str) -> int:
        """Count words in a string."""
        if not text.strip():
            return 0
        return len(text.split())

    def capitalize_words(self, text: str) -> str:
        """Capitalize first letter of each word."""
        return " ".join(word.capitalize() for word in text.split())

    def remove_duplicates(self, text: str) -> str:
        """Remove duplicate characters while maintaining order."""
        seen = set()
        result = []
        for char in text:
            if char not in seen:
                seen.add(char)
                result.append(char)
        return "".join(result)

    def is_palindrome(self, text: str) -> bool:
        """Check if string is a palindrome."""
        cleaned = "".join(char.lower() for char in text if char.isalnum())
        return cleaned == cleaned[::-1]
