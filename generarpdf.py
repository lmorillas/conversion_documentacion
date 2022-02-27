import jinja2
import frontmatter
import markdown
from weasyprint import HTML


with open('proyecto.md') as f:
    post = frontmatter.load(f)

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "plantilla_proyecto.html"
template = templateEnv.get_template(TEMPLATE_FILE)

contenido = markdown.markdown(post.content)
datos = post.to_dict()
datos['contenido'] = contenido
datos['fecha_larga'] = datos['fecha'] #.strftime("%A %d de %B de %Y")


outputText = template.render(datos)


with open('proyecto.html', 'w') as f:
    f.write(outputText)

HTML(string=outputText).write_pdf("proyecto.pdf")