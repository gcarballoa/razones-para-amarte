// Tu lógica de JS aquí
async function cargarRazon() {
    try {
        const response = await fetch('./razones.json');
        const data = await response.json();
        
        // Lógica del día del año
        const ahora = new Date();
        const inicioAnio = new Date(ahora.getFullYear(), 0, 0);
        const dif = ahora - inicioAnio;
        const indiceDia = Math.floor(dif / (1000 * 60 * 60 * 24));
        
        const razonHoy = data.mensajes[indiceDia % data.mensajes.length];
        
        // Inyectar en el HTML
        document.getElementById('reason').innerText = `"${razonHoy.texto}"`;
        document.getElementById('numero-dia').innerText = indiceDia;
        document.getElementById('today').innerText = ahora.toLocaleDateString();
    } catch (e) {
        console.error("Error:", e);
    }
}
cargarRazon();

        


function cerrarPanel() {
    document.getElementById('admin-panel').style.display = 'none';
}
