<template>
  <div id="LoginViewDiv">
    <div id="LoginView">
      <h2>로그인</h2>
      <hr>
      <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="login(credentials)">
        <div>
          <p for="loginform-username">이름ㅤ</p> 
          <input type="text" v-model="credentials.username" id="loginform-username" class="mb-3">
          <p for="loginform-password">비밀번호ㅤ</p> 
          <input type="password" v-model="credentials.password" id="loginform-password" class="mb-3">
          <hr>
          <button id="login-button">로그인</button>
        </div>
      </form>
      <br>
      계정이 없으신가요?ㅤ
      <router-link :to="{ name: 'signup' }" style="color:#170572;">회원가입</router-link>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import AccountErrorList from '@/components/accounts/AccountErrorList.vue'

export default {
  name : 'LoginView',
  components: { AccountErrorList },
  data : function(){
    return {
      credentials:{
        username : '',
        password : '',
      }
    }
  },
  methods : {
    ...mapActions(['login'])
  },
  computed:{
    ...mapGetters(['authError'])
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');

#LoginViewDiv {
  height:100vh;
}

#LoginView{
  align-content: center;
  width: 300px;
  height:auto;
  border: 1px solid; 
  padding:30px; 
  background-color:white; 
  color:black;
  margin:0 auto;
  border-radius: 20px;
  font-family: 'Jua', sans-serif;
}

#loginform-username, #loginform-password{
  background-color: #F7F7F7;
  color:black;
  border-radius: 3px;
  border-width: 1px;
  width: 90%;
  height: 40px;
}

#login-button{
  background-color: #170572;
  width: 60%;
  height: 40px;
  color: white;
  border-width: 0px;
  border-radius: 5px;
}
</style>
