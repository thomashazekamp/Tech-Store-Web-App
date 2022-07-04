const { application } = require('express');
var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/login', function(req, res, next){
  res.render('login')
});

router.get('/logout', function(req, res, next){
  res.render('logout')
});

router.get('/register', function(req, res, next){
  res.render('register')
});

router.get('/order', function(req, res) {
  res.render('order');
});

router.get('/orderhistory', function(req, res) {
  res.render('orderhistory');
});

router.get('/productindividual', function(req, res) {
  res.render('productindividual');
});

router.get('/shoppingbasket', function(req, res) {
  res.render('shoppingbasket');
});

module.exports = router;
