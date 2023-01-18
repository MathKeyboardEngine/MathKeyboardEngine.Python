from typing import Optional

from PyQt6.QtWebEngineWidgets import QWebEngineView


class KatexView(QWebEngineView):
    default_css = 'body { margin: 1px } div { height: 98vh }'

    def __init__(self, latex: Optional[str] = None, css: str = default_css):
        super().__init__()
        self.setHtml(
            r"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/katex@0.15.2/dist/katex.min.css"
      integrity="sha384-MlJdn/WNKDGXveldHDdyRP1R4CTHr3FeuDNfhsLPYrq2t0UBkUdK2jyTnXPEK1NQ"
      crossorigin="anonymous"
    />
    <style>"""
            + css
            + r"""</style>
    <script src="https://cdn.jsdelivr.net/npm/katex@0.15.2/dist/katex.min.js" integrity="sha384-VQ8d8WVFw0yHhCk5E8I86oOhv48xLpnDZx5T9GogA/Y84DcCKWXDmSDfn13bzFZY" crossorigin="anonymous"></script>
    <script type="text/javascript">
      window.addEventListener('DOMContentLoaded', (event) => {
            window.typeSet = function katexRender(latex) {
                katex.render(latex, document.querySelector("div"), { throwOnError: false });
            }
            """
            + (KatexView.__katexRender(latex) if latex else '')
            + r"""
        });
    </script>
  </head>
  <body>
    <div>error</div>
  </body>
</html>"""
        )

    def render(self, latex):
        self.page().runJavaScript(KatexView.__katexRender(latex))

    def __katexRender(latex) -> str:
        return 'window.typeSet(String.raw`' + latex + '`)'
