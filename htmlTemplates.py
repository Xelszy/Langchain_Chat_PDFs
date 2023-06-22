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
}
.chat-message.user .message {
    color: #000;
    background-color: #dcf8c6;
    align-self: flex-end;
}
.chat-message.bot .message {
    background-color: #fff;
    color: #000;
    align-self: flex-start;
}
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