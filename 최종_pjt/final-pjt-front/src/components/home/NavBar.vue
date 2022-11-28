<template>
  <div id="NavBar">

  <nav id="navbar-example2" class="navbar px-4">
      <!-- 메인페이지로 가는 상단 로고 -->
      <div>
        <RouterLink :to="{ name: 'home' }">
          <div class="mx-auto mt-auto">
            <img width=70px class="neumorph" :class="{grayscale:!isHovering}" @mouseover="isHovering = true" @mouseout="isHovering = false" src="@/assets/디즈니이미지-removebg-preview.png" alt="logo to mainpage">
          </div>
        </RouterLink>
      </div>
      <ul class="nav nav-pills">
        <!-- 홈 -->
        <li class="nav-item">
          <router-link to="/" style="text-decoration:none; vertical-align: middle; display: table-cell;"><b></b>&nbsp;</router-link>
        </li>

        <!-- 영화 목록 -->
        <li class="nav-item">
          <b-nav-item-dropdown
            text="영화"
            id="my-nav-dropdown"
            toggle-class="nav-link-custom"
            style="">
          <b-dropdown-item>
            <router-link 
              :to="{ name: 'movies' }"
              style="text-decoration:none;">
              <button type="button" class="btn">전체영화</button>
            </router-link>
          </b-dropdown-item>
          <b-dropdown-item>            
            <router-link 
              to="/random"
              style="text-decoration:none; width:50px;">
              <button type="button" class="btn">랜덤영화</button>
            </router-link>
          </b-dropdown-item>
        </b-nav-item-dropdown>
        </li>

        <li class="nav-item">
          <router-link to="/community" style="text-decoration:none; vertical-align: middle; display: table-cell;"><b>커뮤니티</b>&nbsp;&nbsp;&nbsp;</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="!isLoggedIn" to="/login" style="text-decoration:none; vertical-align: middle; display: table-cell;"><b>로그인</b>&nbsp;&nbsp;&nbsp;</router-link>
        </li>
        <li class="nav-item">
          <router-link v-if="isLoggedIn && username " :to="{ name: 'profile', params: {username} }" style="text-decoration:none; vertical-align: middle; display: table-cell;"><b>마이페이지</b>&nbsp;&nbsp;&nbsp;</router-link>
        </li>
        <li class="nav-item">
          <div class="logout" v-if="isLoggedIn" @click="logout"><b>로그아웃</b></div>
        </li>
      </ul>
    </nav>


  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'

export default {
  name: 'NavBar',
  data() {
    return {
      isHovering: false
    }
  },
  methods: {
    ...mapActions(['logout'])
  },
  computed:{
    ...mapGetters(['isLoggedIn', 'currentUser']),
    username(){
      return this.currentUser.username
    }
  },
}
</script>

<style>
/* nav style */

.navbar {
  /* border: 2px solid blue; */
  background-color:#040714;
  position: sticky;
  top: 0;
  height: 8vh;
  width: 100%;
  display:flex;
  flex-direction:row;
  justify-content: space-between;
  align-items:center;
}

nav a:hover{
  color: #e8c171;
  transition:all.5s;
}

nav a:link{
  color: white;
}

.nav-item {
  color: #e8c171;
  transition:all.5s;
}

li {
  display:table !important;
}

a > span {
  color:#0D6EFD;
  font-weight: bolder;
}

.logout {
  cursor : pointer;
  vertical-align : middle; 
  display : table-cell; 
  color : #0D6EFD;
}

.logout:hover {
  color: #e8c171 !important;
  transition:all.5s;
}

a > span:hover {
  color: #e8c171 !important;
  transition:all.5s;
}

#my-nav-dropdown__BV_toggle_:hover {
  color: white !important;
  transition:all.5s;
}

.dropdown-toggle {
  background-color: transparent !important;
}

#my-nav-dropdown__BV_toggle_menu_{
  min-width:0px !important;
  text-align: center;
}

.input {
    margin: 0 auto;
    justify-content: center;
    align-items: center;
  }
  
  input {
    padding: 1rem;
    border-radius: 1rem;
    border: none;
    outline: none;
    background: #f5f5f5;
    box-shadow: 5px 8px 10px #d1d1d1, -5px -8px 10px #fff;
    color: #bfbfbf;
    transition:0.5s;
  }
  
  input:hover 
  {
    box-shadow: 5px 8px 10px #fff, 5px -8px 5px #d1d1d1;
  }

</style>