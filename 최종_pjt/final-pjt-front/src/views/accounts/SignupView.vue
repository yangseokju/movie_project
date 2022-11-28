<template>
  <div id="SignupViewDiv">
    <div id="SignupView" style="">
      <h2 style=" color: black">회원가입</h2>
      <hr>
      <account-error-list v-if="authError"></account-error-list>
      <form @submit.prevent="signUp(credentials)">
        <p for="signupform-username">아이디</p>
        <input type="text" id="signupform-username" v-model="credentials.username" class="mb-3">
        <p for="signupform-password1">비밀 번호</p> 
        <input type="password" id="signupform-password1" v-model="credentials.password1" class="mb-3">
        <p for="signupform-password2">비밀 번호 확인</p> 
        <input type="password" id="signupform-password2" v-model="credentials.password2" class="mb-3">
        <hr>
        <button id="signup-button">회원가입</button>
      </form>
      <br>
      계정이 있으신가요?ㅤ
      <router-link :to="{ name: 'login' }" style="color: #170572">로그인하러 가기</router-link>
    </div>
  </div>
  </template>
  
  <script>
  import {mapGetters, mapActions} from 'vuex'
  import AccountErrorList from '@/components/accounts/AccountErrorList.vue'
  
  export default {
    name:'SignupView',
    components: { AccountErrorList },
    data(){
      return {
        credentials: {
          username: '',
          password1: '',
          password2: ''
        }
      }
    },
    computed:{
      ...mapGetters(['authError', 'isLoggedIn'])
    },
    methods:{
      ...mapActions(['signUp']),
    }
  }
  </script>
  
  <style>
  @import url('https://fonts.googleapis.com/css2?family=Gowun+Dodum&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=Jua&display=swap');
  
  #SignupViewDiv {
    height:100vh;
  }

  #SignupView{
    align-content: center;
    width: 300px;
    height: auto;
    border: 1px solid; 
    padding:30px; 
    background-color: white; 
    color:black;
    margin:0 auto;
    border-radius: 20px;
    font-family: 'Jua', sans-serif;
  }
  
  #signupform-username, #signupform-password1, #signupform-password2{
    background-color: #F7F7F7;
    border-radius: 3px;
    border-width: 1px;
    width: 90%;
    height: 40px;
    color:black;
  }
  
  #signup-button{
    background-color: #170572;
    width: 60%;
    height: 40px;
    color: white;
    border-width: 0px;
    border-radius: 5px;
  }
  
  </style>
  