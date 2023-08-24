let socket = io();

function scrollToBottom() {
  let messages = document.querySelector('#messages').lastElementChild;
  messages.scrollIntoView();
}

socket.on('connect', function () {
  let searchQuery = window.location.search.substring(1);
  let params = JSON.parse('{"' + decodeURI(searchQuery).replace(/&/g, '","').replace(/\+/g, ' ').replace(/=/g, '":"') + '"}');
  console.log(params);
  socket.emit('join', params, function (err) {
    if (err) {
      alert(err);
      window.location.href = '/';
    } else {
      console.log('No Error');
    }
  })
});

socket.on('disconnect', function () {
  console.log('disconnected from server.');
});




function red() {

  socket.emit('Send to Led', 'SetSoledColor', 'red');
};
function blue() {

  socket.emit('Send to Led', 'SetSoledColor', 'blue');
};

function green() {

  socket.emit('Send to Led', 'SetSoledColor', 'green');
};

function black() {

  socket.emit('Send to Led', 'SetSoledColor', 'black');
};

function gray() {

  socket.emit('Send to Led', 'SetSoledColor', 'gray');
};

function white() {

  socket.emit('Send to Led', 'SetSoledColor', 'white');
};


function updateslider() {

  socket.emit('Send to Led', 'SetBrigthness', document.getElementById("rangee").value);

};


function rgb(r, g, b) {

  var temp = 'rgb(' + [(r || 0), (g || 0), (b || 0)].join(',') + ')';
  return temp
};

function getRGBColor() {
  var r = document.getElementById("rangeeR").value;
  var g = document.getElementById("rangeeG").value;
  var b = document.getElementById("rangeeB").value;

  var q = document.getElementById("can");
  //r,g,b
  q.style.backgroundColor = rgb(g, b, r);
  console.log(q.style.backgroundColor);

  //var temp = rgb(r, b, g);
  //temp = temp.slice(4, temp.length - 1);

  temp = intTohex(r, b, g);
  //temp = temp.toString('16');
  console.log('ss' + temp);
  //b,r,g
  socket.emit('Send to Led', 'SetRGBVAL', temp);
};


function intTohex(r, g, b) {

  var strr = parseInt(r).toString(16);
  var strb = parseInt(b).toString(16);
  var strg = parseInt(g).toString(16);

  if(strr.length == 1)
    strr = "0" + strr;
  if(strg.length == 1)
    strg = "0" + strg;
  if(strb.length == 1)
    strb = "0" + strb;
	

  var te = strr + strg + strb
  console.log(te);
  
  return  te;

 
};




/*
var coun = 0;
function sendJson() {

  function myfunction() {

    console.log(coun);
    if (coun == 0)
      socket.emit('Send to Led', 'SetJson', `{ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,
      d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,
      ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,
      002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff
    }`);
    if (coun == 1)
      socket.emit('Send to Led', 'SetJson', `{002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,
      ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,
      d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,
      ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff

    }`);
    if (coun == 2)
      socket.emit('Send to Led', 'SetJson', `{ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,
        002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,
        ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,
        d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00

    }`);

    if (coun == 2)
      socket.emit('Send to Led', 'SetJson', `{d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,d9ff00,
        ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,ffffff,
        002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,002fff,
        ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000,ff0000

    }`);

    if (coun == 3)
      coun = 0;

    coun++;
  }
  var inttt = setInterval(myfunction(), 1000);



};
*/











/*
socket.on('updateUsersList', function (users) {
  let ol = document.createElement('ol');

  users.forEach(function (user) {
    let li = document.createElement('li');
    li.innerHTML = user;
    ol.appendChild(li);
  });

  let usersList = document.querySelector('#users');
  usersList.innerHTML = "";
  usersList.appendChild(ol);
})

socket.on('newMessage', function (message) {
  const formattedTime = moment(message.createdAt).format('LT');
  const template = document.querySelector('#message-template').innerHTML;
  const html = Mustache.render(template, {
    from: message.from,
    text: message.text,
    createdAt: formattedTime
  });

  const div = document.createElement('div');
  div.innerHTML = html

  document.querySelector('#messages').appendChild(div);
  scrollToBottom();
});

socket.on('newLocationMessage', function (message) {
  const formattedTime = moment(message.createdAt).format('LT');
  console.log("newLocationMessage", message);

  const template = document.querySelector('#location-message-template').innerHTML;
  const html = Mustache.render(template, {
    from: message.from,
    url: message.url,
    createdAt: formattedTime
  });

  const div = document.createElement('div');
  div.innerHTML = html

  document.querySelector('#messages').appendChild(div);
  scrollToBottom();
});

document.querySelector('#submit-btn').addEventListener('click', function (e) {
  e.preventDefault();

  socket.emit("createMessage", {
    text: document.querySelector('input[name="message"]').value
  }, function () {
    document.querySelector('input[name="message"]').value = '';
  })
})

document.querySelector('#send-location').addEventListener('click', function (e) {
  if (!navigator.geolocation) {
    return alert('Geolocation is not supported by your browser.')
  }

  navigator.geolocation.getCurrentPosition(function (position) {
    socket.emit('createLocationMessage', {
      lat: position.coords.latitude,
      lng: position.coords.longitude
    })
  }, function () {
    alert('Unable to fetch location.')
  })
});
*/