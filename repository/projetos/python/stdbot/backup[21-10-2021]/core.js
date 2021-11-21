const discord = require("discord.js");

const client = new discord.Client();

client.on("ready", ()=>{
    console.log(` ${client.user.tag} logado!`);
});

client.on("message", (msg)=>{
    if (msg.content.startsWith("!avatar")) {
        // Send the user's avatar URL

        let usr = msg.mentions.users.first();

        if(usr){
            msg.channel.send("   :scream:  Explanado  :scream:");
            msg.channel.send(usr.displayAvatarURL());
        }

        else{
            msg.channel.send(":thinking: usuario inválido!");
        }

        //msg.channel.send(msg.author.displayAvatarURL());
    }

    if (msg.content.startsWith("!spawn")){

    }
});

client.on("guildMemberAdd", member => {

    const channel = member.guild.channels.cache.find(ch => ch.name === 'bem-vindo');

    if(!channel) return;

    channel.send(`Bem vindo ao servidor ${member}! Escreva um pouco sobre você na ába |apresentação| :wink:`);
})

client.login("ODI5ODM4MjI3MjEyMzM3MTUy.YG99Ew.Ln1fUnBPSaRi3uC5jGDs6YGw4Zo");

