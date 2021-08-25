La pagina fue creada utilizando distintos framework como:
-Django
-Fontawesome
-Bootstrap


Los comentarios dentro del código sólo serán para aclarar pequeños detalles de los cuales creo que son necesarios, pues omitiré entrar en temas sobre las clases de Bootstrap o HTML.

Al utilizar Django podemos crear distintos módulos los cuales ya vienen con archivos predeterminados como “admin.py”,”views.py”, etc. En este documento los archivos de interés, serán aquellos que no conservan su configuración predeterminada.

Para empezar la página fue dividida en módulos dependiendo de su funcionalidad, en este texto trataré de explicar de forma resumida para que sirve cada módulo y en sus respectivos archivos de cada módulo podrá encontrar más información.

De igual forma existen algunos módulos donde sus funciones son muy específicas con sus nombre, por lo cual me parece que son entendibles, por ejemplo “cart_total_amount” que hace referencia a al costo total del carrito, el contenido de la función es muy sencillo

 

La mayoría de módulos contienen archivos llamados:
-”urls.py” (en él encontraremos las urls que tendrá la página y que deberá de hacer al acceder a ellas desde el navegador).
-”app.py” (sirve para poderle dar un nombre al módulo y poder identificarlo dentro de la configuración)
-”views.py” (que daran la funcionalidad a la pagina web)

El módulo de “ config contiene los archivos“:
-“db.py” (solo contiene la configuracion de la conexion de la base de datos)
-”settings.py” (en ella se configuran las rutas de los elementos estáticos, la modulos/apps, el servidor de correo, para más información en el archivo estarán los respectivos comentarios de las partes modificadas)

En el módulo “autenticación” encontraremos:
-”form.py” (crea los campos de un formulario, el cual se verá visible en el navegador)
-”views.py” (contiene las funciones para dar el estilo visual en el navegador)

En el módulo “cart” encontraremos:
-”car_tags.py” (sirve para funciones de conversión)
-”cart.py” (funciones de aumento o decremento del carrito)
-”context _processor.py” (#función para calcular el total del carrito)
-”views.py” (contiene las funciones para aumentar, decrementar, etc )

En el módulo “orders” encontraremos
-”0001_initial.py” (contiene el los modelos para migrar a la base de datos)
-”models.py” (contiene el modelo para agregar productos)

En el módulo “products” encontraremos
-”0001_initial.py” (contiene el los modelos para migrar a la base de datos)
-”models.py” (contiene el modelo para agregar productos)


Los documentos HTML se encuentran en la carpeta template en products

