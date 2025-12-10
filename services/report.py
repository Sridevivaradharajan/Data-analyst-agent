import base64
from jinja2 import Template

def generate_report(df):
    template = """
    <h1>Data Analysis Report</h1>
    <p>Total Rows: {{ rows }}</p>
    <p>Total Columns: {{ cols }}</p>
    <h2>Preview</h2>
    {{ preview }}
    """

    html = Template(template).render(
        rows=len(df),
        cols=len(df.columns),
        preview=df.head(5).to_html()
    )

    encoded = base64.b64encode(html.encode()).decode()
    return {"report_html_base64": encoded}
