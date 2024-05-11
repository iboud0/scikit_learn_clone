# Testing/test_impute_missing_values_mean.py
import sys
sys.path.append('C:\\Users\\Pc\\Downloads\\scikit-learn-clone')
import unittest
import numpy as np
from preprocessing.impute_missing_values_mean import impute_missing_values_mean



class TestImputeMissingValuesMean(unittest.TestCase):

    def test_impute_missing_values_mean_custom(self):
        X = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
        X_imputed_custom = impute_missing_values_mean(X)
        expected_custom = np.array([[1., 2., 7.5], [4., 5., 6.], [7., 8., 9.]])
        self.assertTrue(np.allclose(X_imputed_custom, expected_custom, equal_nan=True))

    def test_impute_missing_values_mean_sklearn(self):
        from sklearn.impute import SimpleImputer
        X = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
        imputer_sklearn = SimpleImputer(strategy='mean')
        X_imputed_sklearn = imputer_sklearn.fit_transform(X)
        expected_sklearn = np.array([[1., 2., 7.5], [4., 5., 6.], [7., 8., 9.]])
        self.assertTrue(np.allclose(X_imputed_sklearn, expected_sklearn, equal_nan=True))

if __name__ == '__main__':
    unittest.main()