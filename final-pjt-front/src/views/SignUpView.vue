<template>
  <div>
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
    </div>
    <h3 class="fs-2"><b>Sign Up</b></h3>
    <div class="dummy-box">
    </div>
    <div class="dummy-box">
    </div>
    <form @submit.prevent="signUp">
      <b class="username">아이디</b><br>
      <span class="input" >
        <input type="text" id="username" v-model="username" placeholder="아이디">
        <span></span><br>
      </span>
      <br>
      <b class="password1">비밀번호</b><br>
      <span class="input" >
        <input type="password" id="password1" v-model="password1" placeholder="비밀번호">
        <span></span><br>
      </span>
      <br>
      <b class="password2">비밀번호 확인</b><br>
      <span class="input" >
        <input type="password" id="password2" v-model="password2" placeholder="비밀번호 확인">
        <span></span><br>
      </span>
      <br>
      <br>
      <div>
        <button class="sign_up glow-on-hover" type="submit" value="SignUp">회원가입</button>
      </div>
      
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        // username,
        // password1,
        // password2,
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)

    }
  }
}
</script>

<style lang="scss" scoped>
::-webkit-input-placeholder {
        text-align: center;
}
.input {
  
  // needs to be relative so the :focus span is positioned correctly
  position:relative;
  
  // bigger font size for demo purposes
  // font-size: 1.5em;
  
  // the border gradient
  background: linear-gradient(21deg, #10abff, #1beabd);
  
  // the width of the input border
  padding: 3px;
  
  // we want inline fields by default
  display: inline-block;
  
  // we want rounded corners no matter the size of the field
  border-radius: 9999em;
  
  // style of the actual input field
  *:not(span) {
    position: relative;
    display: inherit;
    border-radius: inherit;
    margin: 0;
    border: none;
    outline: none;
    padding: 2 .325em;
    z-index: 1; // needs to be above the :focus span
    
    // summon fancy shadow styles when focussed
    &:focus + span {
      opacity: 1;
      transform: scale(1);
    }
  }
  
  // we don't animate box-shadow directly as that can't be done on the GPU, only animate opacity and transform for high performance animations.
  span {
    
    transform: scale(.993, .94); // scale it down just a little bit
    transition: transform .5s, opacity .25s;
    opacity: 0; // is hidden by default
    height:50% !important;
    
    position:absolute;
    z-index: 0; // needs to be below the field (would block input otherwise)
    margin:4px; // a bit bigger than .input padding, this prevents background color pixels shining through
    left:0;
    top: 0.2em;;
    right:0;
    bottom:0;
    border-radius: inherit;
    pointer-events: none; // this allows the user to click through this element, as the shadow is rather wide it might overlap with other fields and we don't want to block those.
    
    // fancy shadow styles
    box-shadow: inset 0 0 0 3px #fff,
      0 0 0 4px #fff,
      3px -3px 30px #1beabd, 
      -3px 3px 30px #10abff;
  }
}

.input-info {
  height: 30%;
}
div{
    text-align: center;
}
.input {
  
  // needs to be relative so the :focus span is positioned correctly
  position:relative;
  
  // bigger font size for demo purposes
  // font-size: 1.5em;
  
  // the border gradient
  background: linear-gradient(21deg, #10abff, #1beabd);
  
  // the width of the input border
  padding: 3px;
  
  // we want inline fields by default
  display: inline-block;
  
  // we want rounded corners no matter the size of the field
  border-radius: 9999em;
  
  // style of the actual input field
  *:not(span) {
    position: relative;
    display: inherit;
    border-radius: inherit;
    margin: 0;
    border: none;
    outline: none;
    padding: 2 .325em;
    z-index: 1; // needs to be above the :focus span
    
    // summon fancy shadow styles when focussed
    &:focus + span {
      opacity: 1;
      transform: scale(1);
    }
  }
  
  // we don't animate box-shadow directly as that can't be done on the GPU, only animate opacity and transform for high performance animations.
  span {
    
    transform: scale(.993, .94); // scale it down just a little bit
    transition: transform .5s, opacity .25s;
    opacity: 0; // is hidden by default
    
    position:absolute;
    z-index: 0; // needs to be below the field (would block input otherwise)
    margin:4px; // a bit bigger than .input padding, this prevents background color pixels shining through
    left:0;
    top:0;
    right:0;
    bottom:0;
    border-radius: inherit;
    pointer-events: none; // this allows the user to click through this element, as the shadow is rather wide it might overlap with other fields and we don't want to block those.
    
    // fancy shadow styles
    box-shadow: inset 0 0 0 3px #fff,
      0 0 0 4px #fff,
      3px -3px 30px #1beabd, 
      -3px 3px 30px #10abff;
  }
}
.glow-on-hover {
    width: 150px;
    height: 50px;
    border: none;
    outline: none;
    color: #fff;
    background: #111;
    cursor: pointer;
    position: relative;
    z-index: 0;
    border-radius: 10px;
}

.glow-on-hover:before {
    content: '';
    background: linear-gradient(45deg, #ff0000, #ff7300, #fffb00, #48ff00, #00ffd5, #002bff, #7a00ff, #ff00c8, #ff0000);
    position: absolute;
    top: -2px;
    left:-2px;
    background-size: 400%;
    z-index: -1;
    filter: blur(5px);
    width: calc(100% + 4px);
    height: calc(100% + 4px);
    animation: glowing 20s linear infinite;
    opacity: 0;
    transition: opacity .3s ease-in-out;
    border-radius: 10px;
}

.glow-on-hover:active {
    color: #000
}

.glow-on-hover:active:after {
    background: transparent;
}

.glow-on-hover:hover:before {
    opacity: 1;
}

.glow-on-hover:after {
    z-index: -1;
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: #111;
    left: 0;
    top: 0;
    border-radius: 10px;
}
@keyframes glowing {
    0% { background-position: 0 0; }
    50% { background-position: 400% 0; }
    100% { background-position: 0 0; }
}
</style>
