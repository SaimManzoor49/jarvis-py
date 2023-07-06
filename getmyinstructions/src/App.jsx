import React, { useEffect, useState } from 'react';

const App = () => {
  const [message, setMessage] = useState('');
  const [listening, setListening] = useState(false);
  const recognition = new window.webkitSpeechRecognition();

  useEffect(() => {
    recognition.continuous = true;
    recognition.interimResults = true;
    recognition.lang = 'en-US';

    recognition.onresult = (event) => {
      const transcript = Array.from(event.results)
        .map((result) => result[0])
        .map((result) => result.transcript)
        .join('');
      // setMessage(transcript);

      const temp =  transcript.toLowerCase()
      setMessage(temp);
    };

    return () => {
      recognition.stop();
    };
  }, []);

  const startListening = () => {
    recognition.start();
    setListening(true);
  };

  const stopListening = () => {
    recognition.stop();
    setListening(false);
  };

  const sendVoiceMessage = async() => {
    console.log(message)
// ///////////////////////////////////////////////////////////////////////
    

   await fetch('http://127.0.0.1:5000/api/voice-command', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message }),
    })
      .then((response) => {
        
        // console.log(response.json())
      return  response.json()
      
      })
      .then((data) => {
        console.log(data); // Handle the response from the server
      })
      .catch((error) => {
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Voice Recognition</h1>
      <p>{message}</p>
      {listening ? (
        <button onClick={stopListening}>Stop Listening</button>
      ) : (
        <button onClick={startListening}>Start Listening</button>
      )}
      <button onClick={sendVoiceMessage}>Send Message</button>
    </div>
  );
};

export default App;
