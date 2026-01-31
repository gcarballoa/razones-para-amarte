// Función para guardar en LocalStorage
function guardarPersonalizacion() {
    const fecha = document.getElementById('custom-date').value; // Formato "DD/MM"
    const texto = document.getElementById('custom-text').value;
    const cat = document.getElementById('custom-cat').value;

    const misRazones = JSON.parse(localStorage.getItem('misRazones') || '{}');
    misRazones[fecha] = { texto, categoria: cat };
    
    localStorage.setItem('misRazones', JSON.stringify(misRazones));
    alert("¡Mensaje guardado para el " + fecha + "!");
    location.reload(); // Recargar para ver cambios
}

// Lógica de carga actualizada
async function cargarRazon() {
    const ahora = new Date();
    const diaMes = `${ahora.getDate()}/${ahora.getMonth() + 1}`; // Ejemplo: "30/1"
    
    // 1. Revisar si hay algo personalizado para hoy
    const personalizados = JSON.parse(localStorage.getItem('misRazones') || '{}');
    
    if (personalizados[diaMes]) {
        mostrarEnPantalla(personalizados[diaMes].texto, "Personalizado");
    } else {
        // 2. Si no hay, cargar del JSON original
        const response = await fetch('./razones.json');
        const data = await response.json();
        
        // Lógica del día del año
        const ahora = new Date();
        const inicioAnio = new Date(ahora.getFullYear(), 0, 0);
        const dif = ahora - inicioAnio;
        const indiceDia = Math.floor(dif / (1000 * 60 * 60 * 24));
        
        const razonHoy = data.mensajes[indiceDia % data.mensajes.length];
        mostrarEnPantalla(razonHoy.texto, razonHoy.categoria);
    }
}
cargarRazon();
     

function mostrarEnPantalla(texto, categoria) {
    document.getElementById('reason').innerText = `"${texto}"`;
    document.getElementById('numero-dia').innerText = categoria;
}