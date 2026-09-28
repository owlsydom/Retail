# Uso de IA

Este documento registra las consultas reales realizadas durante el trabajo del catálogo. Se usaron 3 de los 5 prompts permitidos.

## Consultas y respuestas

1. **Prompt:** “Puedes cambiar el color a una combinacion leve entre amarillo y naranja? ...” La solicitud completa pidió conservar el diseño, cambiar la portada, sus textos y asignar colores a las secciones.
   **Resumen de la respuesta:** Se ajustó la paleta de la portada, se creó una estrella amarilla conectada por cables y se definieron acentos diferenciados para cada sección.

2. **Prompt:** “tengo la duda, por que no se ve la imagen de precios? porfavor ayudame”
   **Resumen de la respuesta:** Se detectó que la plantilla buscaba el GIF en una carpeta equivocada; se corrigió la ruta para apuntar al archivo existente en `static/GIF/precio.gif`.

3. **Prompt:** “ahora necesito integrar lo siguiente a este proyecto, ten en cuenta que lo del minimarket se debe integrar a este. es decir, este debe quedar tal cual con el mismo diseño solo que debe cambiar a una pagina de minimarket...” La solicitud detalló las apps PrincipalApp, NegocioApp y CategoriasApp, productos JSON, resumen de stock, navegación y uso de IA.
   **Resumen de la respuesta:** Se propuso integrar las tres apps al proyecto existente, cargar 20 productos desde JSON, calcular disponibilidad en la vista y crear páginas responsivas conservando la línea visual del sitio.

4. **Prompt:** “disculpa, requiero que para agregar, eliminar o modificar los productos vuelva a ser mediante la base de datos de django ingresando con mi user y contraseña. No quiero que la base de datos este solo en el json.”
   **Resumen de la respuesta:** Se propuso guardar productos con un modelo Django, administrarlos desde `/admin/` con autenticación y transferir los registros existentes del JSON a la base de datos mediante una migración inicial.

## Cómo se utilizó la IA

Se pidió ayuda primero para adaptar los colores y la portada del sitio; después, para corregir una imagen que no cargaba; y finalmente, para convertir el sitio en un catálogo de minimarket. La IA ayudó a localizar las rutas y estilos existentes, organizar las nuevas aplicaciones, proponer los datos iniciales y preparar las vistas y páginas. Los productos se importaron inicialmente desde JSON, pero ahora la base de datos de Django es la fuente activa y se administran con una cuenta autenticada.

**Nota para la entrega:** revisa esta explicación y ajusta las frases a tus propias palabras, especialmente cualquier decisión que hayas tomado o cambiado durante la evaluación.