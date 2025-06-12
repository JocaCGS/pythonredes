const WebSocket = require('ws');

const conexaolanlegal = new WebSocket.Server({ port: 4000})


// todo -> encerrrar sv e cleinet
conexaolanlegal.on('connection', (ws)=> {
    console.log("Cliente Conectado");
    
    
    ws.on('message', (message) =>{
        console.log(`Recebido do Cliente: ${message}`);        
        ws.send(`Echo: ${message}`);
    });


    ws.on('close', () => {
        console.log("Cliente Desconectado");
    });

    ws.on('error', (err) =>{
        console.log(`Erro: ${err}`);
    });

});


console.log('Servidor WebSocket Rodando em ws://localhost:8080')