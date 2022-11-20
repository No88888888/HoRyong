<template>
  <div>
    <h1>Movie Page</h1>
    <hr>
    <MovieLists/>
    <div class="example-modal-window">
    <p>버튼을 누르면 모달 대화 상자가 열립니다.</p>
    <button @click="openModal">열기</button>

    <!-- 컴포넌트 MyModal -->
    <ReviewModal @close="closeModal" v-if="modal">
      <!-- default 슬롯 콘텐츠 -->
      <p>영화의 리뷰를 입력해서 다른 영화를 추천 받아 보세요!</p>
      <div><input v-model="message"></div>
      <!-- /default -->
      <!-- footer 슬롯 콘텐츠 -->
      <template slot="footer">
        <button @click="doSend">제출</button>
      </template>
      <!-- /footer -->
    </ReviewModal>
  </div>
  </div>
</template>

<script>
import MovieLists from '@/components/MovieLists'
import ReviewModal from '@/components/ReviewModal'
export default {
    name : 'MovieView',
    components: {
        MovieLists,
        ReviewModal,
    },
    data() {
      return {
        modal: false,
        message: ''
      }
    },
    methods: {
      openModal() {
        this.modal = true
      },
      closeModal() {
        this.modal = false
      },
      doSend() {
        if (this.message.length > 0) {
          alert(this.message)
          this.message = ''
          this.closeModal()
        } else {
          alert('메시지를 입력해주세요.')
        }
      }
    }    
}
</script>

<style>

</style>