 module.exports = function(grunt) {
  //配置参数
  grunt.initConfig({
     pkg: grunt.file.readJSON('package.json'),
     concat: {
         options: {
             separator: ';',
             stripBanners: true
         },
         dist: {    
             src: [
                "static/libs/jquery/jquery/dist/jquery.js",
                "static/libs/angular/angular/angular.js",
                "static/libs/angular/angular-animate/angular-animate.js",
                "static/libs/angular/angular-cookies/angular-cookies.js",
                "static/libs/angular/angular-messages/angular-messages.js",
                "static/libs/angular/angular-resource/angular-resource.js",
                "static/libs/angular/angular-sanitize/angular-sanitize.js",
                "static/libs/angular/angular-touch/angular-touch.js",
                "static/libs/angular/angular-ui-router/release/angular-ui-router.js",
                "static/libs/angular/ngstorage/ngStorage.js",
                "static/libs/angular/angular-bootstrap/ui-bootstrap-tpls.js",
                "static/libs/angular/oclazyload/dist/ocLazyLoad.js",
                "static/app/js/app.js",
                "static/app/js/config.js",
                "static/app/js/config.lazyload.js",
                "static/app/js/config.router.js",
                "static/app/js/main.js",
                "static/app/js/services/service.shop.js",
                "static/app/js/services/ui-load.js"
             ],
             dest: "static/app/js/default.js"
         }
     },
     uglify: {
         options: {
         },
         dist: {
             files: {
                 'static/app/js/app.min.js': 'static/app/js/default.js'
             }
         }
     },
     cssmin: {
         options: {
             keepSpecialComments: 0
         },
         compress: {
             files: {
                 'assets/css/default.css': [
                     "css/global.css",
                     "css/pops.css",
                     "css/index.css"
                 ]
             }
         }
     }
  });

  //载入concat和uglify插件，分别对于合并和压缩
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-cssmin');

  //注册任务
  grunt.registerTask('default', ['concat', 'uglify', 'cssmin']);
  // grunt.registerTask('default', ['concat']);
}