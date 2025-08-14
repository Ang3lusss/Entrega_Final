# Not Today — Proyecto Final Django (Coderhouse)

Aplicación web estilo blog + catálogo desarrollada como proyecto final del curso de Python/Django en Coderhouse.

Incluye autenticación, perfiles con avatar, CRUD de páginas tipo blog y CRUD de prendas, todo con control de acceso y uso de CKEditor para texto enriquecido.

## Descripción personal (About)

¡Hola! Soy Matias Vigil, tengo 44 años y me inscribí en el curso de Python de Coderhouse como complemento a una tesis de licenciatura que estoy terminando.

También soy creador de Not Today, un espacio que fusiona lo gótico, el K-pop y lo geek en un mismo lugar. Me apasiona la programación, el diseño web y la idea de combinar distintas culturas y estilos en un solo proyecto.

---

## Funcionalidades principales

- **Home** (`/`)
- **About** (`/about/`) con mi descripción personal.
- **Pages** (`/pages/`)
  - Listado con mensaje *"No hay páginas aún"* si está vacío.
  - Detalle individual (`/pages/<id>/`).
  - Crear, editar y borrar (solo usuarios logueados).
- **Catálogo de prendas** (`/prendas/`)
  - Listado de prendas con imagen.
  - Crear, editar, borrar (solo logueados).
- **Autenticación**:
  - Registro (`/accounts/signup/`), login (`/accounts/login/`), logout (`/accounts/logout/`).
- **Perfil de usuario**:
  - Ver perfil (`/accounts/profile/`).
  - Editar datos personales y avatar.
  - Cambio de contraseña.

---

## Tecnologías y librerías

- Python 3.13
- Django 5.2.4
- Pillow
- django-ckeditor

---

## Estructura de apps

- `pages/` — Home, About, Blog (Pages)
- `app_local_ropa/` — Prendas (modelo principal del CRUD)
- `accounts/` — Autenticación y perfiles

---
