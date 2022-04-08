var models = []
var index = 0

var settings = {
  duration : '10000',
};

document.querySelectorAll('.carousel-item').forEach(function(item){
  models.push(item);
});

// ilk model aktif ediliyor.
models[index].classList.add('active');

// düzenli olarak değiştrme
setInterval(function(){
  index++;

  if(models.length  == index ){
    index = 0
  }

  models[index].classList.add('active');

  for (var i = 0; i < models.length; i++) {
    models[i]
  }

  if (index == 0) {
    if (models[models.length-1].classList.contains("active")) {
      models[models.length-1].classList.remove('active');
    }
  } else {
    if (models[index-1].classList.contains("active")) {
      models[index-1].classList.remove('active');
    }
  }

},settings.duration)
