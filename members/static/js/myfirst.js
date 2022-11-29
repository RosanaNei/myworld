function myHalt() {
    alert("Hello from a static file!");
  }

  const p = document.getElementById("libros"); // Encuentra el elemento de párrafo en la página a través de su id "foo"
  p.onclick = mostrarAlerta; // Agrega la función onclick al elemento
    
  function mostrarAlerta(evento) {
    alert("¡Evento onclick activado!");
  }

  /*function mostrarAlerta(evento){
    var img = getElementById('libros');
    if(img.className == 'libros'){
      img.className = 'libros-grande';
    }else{
      img.className = 'libros';
    }
  }*/