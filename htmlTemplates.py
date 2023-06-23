css = '''
<style>
    .chat-message {
        padding: 10px;
        margin-bottom: 10px;
        display: flex;
        align-items: flex-start;
    }

    .chat-message.user {
        justify-content: flex-end;
    }

    .chat-message.bot {
        justify-content: flex-start;
    }

    .chat-message .avatar {
        display: none;
    }

    .chat-message .message {
        max-width: 70%;
        padding: 10px;
        border-radius: 10px;
        color: #fff;
        word-wrap: break-word;
        backdrop-filter: blur(10px); /* Efek glassmorphism */
        background-color: rgba(255, 255, 255, 0.2); /* Warna latar belakang dengan transparansi */
    }

    .chat-message.user .message {
        color: #000;
        align-self: flex-end;
        background-color: rgba(220, 248, 198, 0.5); /* Warna latar belakang user */
    }

    .chat-message.bot .message {
        color: #000;
        align-self: flex-start;
        background-color: rgba(255, 255, 255, 0.5); /* Warna latar belakang bot */
    }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/cN0nmSj/Screenshot-2023-05-28-at-02-37-21.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
