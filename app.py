import streamlit as st

# Código HTML a visualizar
html_code = """
<!-- Widget JavaScript bundle -->
<script src="https://cloud.google.com/ai/gen-app-builder/client?hl=es_419"></script>

<!-- Search widget element is not visible by default -->
<gen-search-widget
  configId="eda82364-8747-4f13-8504-0d6f1aaa3526"
  triggerId="searchWidgetTrigger">
</gen-search-widget>

<!-- Element that opens the widget on click. It does not have to be an input -->
<input placeholder="Search here" id="searchWidgetTrigger" />
"""

# Renderizar el código HTML en Streamlit
st.components.v1.html(html_code, height=500)
