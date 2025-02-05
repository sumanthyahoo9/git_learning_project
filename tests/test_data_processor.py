# src/data_processor.py
from typing import List, Dict, Any
from statistics import mean, median

class DataProcessor:
    """
    Data Processing module
    """
    def calculate_statistics(self, numbers: List[float]) -> Dict[str, float]:
        """Calculate basic statistics for a list of numbers."""
        if not numbers:
            raise ValueError("List cannot be empty")
        
        return {
            "mean": mean(numbers),
            "median": median(numbers),
            "min": min(numbers),
            "max": max(numbers)
        }
    
    def filter_by_threshold(self, numbers: List[float], threshold: float) -> List[float]:
        """Filter numbers greater than threshold."""
        return [num for num in numbers if num > threshold]
    
    def group_by_property(self, items: List[Dict[str, Any]], property_name: str) -> Dict[Any, List[Dict[str, Any]]]:
        """Group items by a property."""
        result = {}
        for item in items:
            if property_name not in item:
                raise KeyError(f"Property {property_name} not found in item")
            key = item[property_name]
            if key not in result:
                result[key] = []
            result[key].append(item)
        return result
    
    def find_duplicates(self, items: List[Any]) -> List[Any]:
        """Find duplicate items in a list."""
        seen = set()
        duplicates = set()
        for item in items:
            if item in seen:
                duplicates.add(item)
            seen.add(item)
        return list(duplicates)
    
    def transform_data(self, data: List[Dict[str, Any]], transformations: Dict[str, callable]) -> List[Dict[str, Any]]:
        """Apply transformations to data fields."""
        result = []
        for item in data:
            transformed_item = {}
            for key, value in item.items():
                if key in transformations:
                    transformed_item[key] = transformations[key](value)
                else:
                    transformed_item[key] = value
            result.append(transformed_item)
        return result