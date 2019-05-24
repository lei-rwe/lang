import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    df = np.random.randn(2, 4)
    print(df)
    tips = sns.load_dataset('tips')
    print(tips.shape)
    sns.distplot(tips['total_bill'])
    plt.show()

if __name__ == '__main__':
    main()