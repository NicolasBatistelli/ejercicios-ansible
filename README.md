# Ejercitación Ansible - Todos los Niveles

Esta colección de ejercicios está diseñada para practicar y dominar el uso de Ansible en tres niveles de complejidad: Principiante, Intermedio y Avanzado. Cada nivel contiene 15 ejercicios prácticos para mejorar tus habilidades.

---

## Contenido

### 1. Nivel Principiante (15 ejercicios)
1. **Instalar paquetes básicos:**  
   Crea un playbook que instale un paquete específico (como `vim` o `git`) en un servidor.  
2. **Iniciar y detener servicios:**  
   Escribe un playbook que inicie un servicio como `nginx` y otro que lo detenga.  
3. **Crear y copiar archivos:**  
   Crea un archivo simple en un servidor y copia un archivo desde el host local al servidor remoto.  
4. **Actualizar el sistema:**  
   Crea un playbook que actualice los paquetes del sistema usando `apt` o `yum`.  
5. **Cambiar permisos de archivos:**  
   Cambia los permisos de un archivo en el servidor remoto usando Ansible.  
6. **Comprobar conectividad:**  
   Usa el módulo `ping` para verificar que todos los hosts en tu inventario están accesibles.  
7. **Configurar variables:**  
   Define una variable en un playbook para instalar una lista de paquetes y reutilízala.  
8. **Gestionar usuarios y grupos:**  
   Crea un playbook que añada un nuevo usuario y lo añada a un grupo.  
9. **Eliminar archivos:**  
   Crea un playbook que elimine archivos específicos en el servidor remoto.  
10. **Crear directorios:**  
    Crea un playbook que cree un directorio si no existe.  
11. **Comprobar contenido de archivos:**  
    Usa el módulo `lineinfile` para asegurarte de que una línea específica esté presente en un archivo.  
12. **Gestionar variables del entorno:**  
    Define variables de entorno en el servidor usando Ansible.  
13. **Ejecución de comandos ad-hoc:**  
    Usa Ansible para ejecutar un comando ad-hoc en el servidor, como `uptime` o `df -h`.  
14. **Instalar Apache:**  
    Crea un playbook que instale y configure Apache en un servidor.  
15. **Configurar el firewall:**  
    Configura reglas básicas del firewall (como abrir el puerto 80) utilizando el módulo `ufw`.

---

### 2. Nivel Intermedio (15 ejercicios)
1. **Desplegar una aplicación web simple:**  
   Crea un playbook que instale un servidor web y despliegue una página HTML.  
2. **Usar plantillas Jinja2:**  
   Crea una plantilla de configuración (`.j2`) que use variables y aplícalas a un servidor.  
3. **Gestionar múltiples servidores:**  
   Usa un inventario con al menos dos grupos de servidores y ejecuta tareas diferentes en cada uno.  
4. **Usar handlers:**  
   Configura un handler para que reinicie un servicio solo si cambia el archivo de configuración.  
5. **Configurar SSH con claves:**  
   Crea un playbook que copie claves SSH en los servidores para permitir autenticación sin contraseña.  
6. **Usar bucles:**  
   Escribe un playbook que use `with_items` para instalar una lista de paquetes en los servidores.  
7. **Configurar tareas condicionales:**  
   Define una tarea que solo se ejecute si el sistema operativo es Ubuntu.  
8. **Backup de archivos antes de modificarlos:**  
   Configura un playbook que cree una copia de seguridad de archivos antes de modificarlos.  
9. **Desplegar bases de datos:**  
   Despliega una base de datos MySQL o PostgreSQL en un servidor utilizando Ansible.  
10. **Configurar cron jobs:**  
    Crea un cron job en el servidor que ejecute un script todos los días a las 2:00 AM.  
11. **Instalar Docker:**  
    Escribe un playbook para instalar Docker en servidores remotos.  
12. **Trabajar con roles:**  
    Crea un rol en Ansible que gestione la instalación y configuración de Apache.  
13. **Usar vaults de Ansible:**  
    Protege contraseñas o claves sensibles usando Ansible Vault.  
14. **Comprobar el estado de un servicio:**  
    Crea un playbook que verifique si un servicio está corriendo y lo inicie si está detenido.  
15. **Configurar variables según el sistema operativo:**  
    Configura diferentes tareas o variables para sistemas basados en Debian y RedHat.

---

### 3. Nivel Avanzado (15 ejercicios)
1. **Desplegar aplicaciones en Docker:**  
   Despliega una aplicación completa en un contenedor Docker utilizando Ansible.  
2. **Automatizar el despliegue de una pila LAMP/LEMP:**  
   Crea un playbook que instale y configure la pila LAMP (Linux, Apache, MySQL, PHP) o LEMP (Nginx en lugar de Apache).  
3. **Configuración de un clúster de Kubernetes:**  
   Usa Ansible para desplegar un clúster básico de Kubernetes.  
4. **Automatización de certificados SSL:**  
   Usa Ansible para automatizar la generación e instalación de certificados SSL.  
5. **Desplegar aplicaciones en la nube (AWS, Azure, etc.):**  
   Crea un playbook que gestione servidores y recursos en la nube (por ejemplo, crear instancias EC2 en AWS).  
6. **Uso de fact gathering avanzado:**  
   Utiliza los facts que recoge Ansible para tomar decisiones dinámicas en los playbooks.  
7. **Optimización con asynchronous actions:**  
   Configura tareas asíncronas en Ansible para ejecutar acciones más rápidas.  
8. **Despliegue continuo con Ansible y Jenkins:**  
   Configura un pipeline en Jenkins que use Ansible para automatizar despliegues.  
9. **Configurar balanceadores de carga:**  
   Usa Ansible para configurar un balanceador de carga (como Nginx o HAProxy).  
10. **Orquestar actualizaciones de sistemas en paralelo:**  
    Realiza actualizaciones en múltiples servidores de manera orquestada, asegurándote de que siempre haya servidores disponibles.  
11. **Automatización de redes (Cisco, Juniper):**  
    Usa módulos de red de Ansible para gestionar switches y routers de manera automatizada.  
12. **Gestión de almacenamiento:**  
    Configura volúmenes LVM y monta sistemas de archivos en los servidores.  
13. **Configuración de entornos multi-stage (desarrollo, staging, producción):**  
    Crea un inventario que gestione diferentes entornos (dev, staging, prod) y defina diferentes configuraciones según el entorno.  
14. **Automatización avanzada con filtros y plugins personalizados:**  
    Crea y usa filtros y plugins personalizados en Ansible para realizar tareas avanzadas.  
15. **Desplegar aplicaciones con microservicios:**  
    Configura y despliega una aplicación distribuida en microservicios usando contenedores y Ansible.

---
