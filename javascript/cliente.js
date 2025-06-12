const net = require('net');

let lancha = 4000

const input = document.getElementById("mensagem_cliente")

let msgCliente = input.textContent

const client = net.createConnection({port: lancha}, ()=>{
    console.log(`Conectado ao servidor ${lancha}`)
    client.write(`Mensagem: ${msgCliente}`)
})

client.on('data', (data)=>{
    console.log(`Log do servidor: ${data}`)
    client.end()
})

client.on('end', (end) =>{
    console.log('Desconectado')
})

