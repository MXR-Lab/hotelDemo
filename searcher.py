import numpy as np
import csv

class Searcher:
    def __init__(self, indexPath):
        self.indexPath = indexPath

    def search(self, queryFeatures, limit = 5):
        results = {}

        #Open index file
        with open(self.indexPath) as f:
            #initialize csv reader
            reader = csv.reader(f)

            #Loop over each row in the index
            for row in reader:
                #Parse imageID and features then compute the chi-squared dist to compare
                features = [float(x) for x in row[1:]]
                d = self.chi2_distance(features, queryFeatures)

                #Update the result dictionary
                results[row[0]] = d

            f.close()

        #Sort results so most relevant images appear first
        results = sorted([(v,k) for (k,v) in results.items()])

        return results[:limit]
    
    def chi2_distance(self, histA, histB, eps = 1e-10):
        d = 0.5 * np.sum([((a-b) ** 2) / (a + b + eps) for (a,b) in zip(histA, histB)])
        return d