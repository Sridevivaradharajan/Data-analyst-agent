import matplotlib.pyplot as plt
import base64
from io import BytesIO

def chart_to_base64():
    buffer = BytesIO()
    plt.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
    plt.clf()
    return img_base64

def generate_histogram(df, column):
    df[column].plot(kind="hist", title=f"Histogram of {column}")
    return chart_to_base64()

def generate_correlation_heatmap(df):
    import seaborn as sns
    sns.heatmap(df.corr(), annot=False)
    return chart_to_base64()
