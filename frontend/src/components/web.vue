<template>
  <div class="web">
    <div class='method'>
      <div class='method-title'>
        <h2>在网站中嵌入web咨询页面地址</h2>
      </div>
      <div class='method-background'>
        <div class='method-content'>
          <a>{{ webUrl }}</a>
        </div>
        <div class='method-foot'>
          <ul>
            <li>企业配置桌面web客服页面接入，可参考<a href='http://192.168.55.33:8000/documentation/#/web'>《桌面网站web页面接入》</a></li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'web',
  data () {
    return {
      webUrl: '',
      apiadminShowUrlStatus: '../api/admin_show_url_status/'
    }
  },
  methods: {
    /**
      * @description 获取企业web端接入网址
      */
    getWebUrlApi () {
      this.$http.post(this.apiadminShowUrlStatus)
        .then((response) => {
          if (response.data === 'ERROR, session is broken.') {
            window.location.href = '../en_login/'
          } else if (response.data === 'ERROR, wrong email.') {
            window.location.href = '../en_login/'
          } else {
            this.webUrl = response.data.web_url
          }
        })
    }
  },
  created () {
    this.getWebUrlApi()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.web {
  padding: 0em 3em;
}

.method {
  margin: 4em 0em;
  border: 1px solid #d7dde4;
  border-radius: 4px;
}

.method-title {
  padding: 0.5em 2em;
  border-bottom: 1px solid #d7dde4;
}

.method-content {
  margin: 0.5em 2em;
  margin-top: 0em;
  padding: 1em 1em;
  background-color: #dddee1;
}

.method-foot {
  padding: 0.5em 2em;
  padding-bottom: 1em;
}

.method-background {
  padding-top: 1em;
  background-color: #f5f7f9;
}
</style>
