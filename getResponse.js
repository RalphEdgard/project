var XMLHttpRequest = require('xhr2');
var xhr = new XMLHttpRequest();

xhr.open("POST", 'https://chat.openai.com/chat/6bc2342e-ac4b-42c3-b68e-b81562abd11f', true);
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4)  { 
    var serverResponse = xhr.responseText;
    console.log(serverResponse);
  }
};
xhr.send(null);
