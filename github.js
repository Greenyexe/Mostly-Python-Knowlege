function calculateDatsBetweenDates(begin, end) {
  var beginDate = new Date(begin);
  var endDate = new Date(end);
  var millisecondsPerDay = 1000 * 60 * 60 * 24;
  var millisBetween = endDate.getTime() - beginDate.getTime();
  var days = millisBetween / millisecondsPerDay;
  return Math.floor(days);
}

// find all images without alternate text
// and give them a red border
function thing() {
  var images = document.getElementsByTagName('img');
  for (var i = 0; i < images.length; i++) {
    if (images[i].alt == '') {
      images[i].style.border = '3px solid red';
    }
  }
}

// print 58 * 32
function print() {
  var result = 58 * 32;
  console.log(result);
}

print();