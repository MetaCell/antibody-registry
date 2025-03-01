const { merge } = require('webpack-merge');
const common = require('./webpack.config.js');

var path = require('path');

const PORT = 9000;


module.exports = env => {

  const theDomain = env && env.DOMAIN ? env.DOMAIN : 'localhost:5000';
  
  console.log('Dev server address: ', theDomain);

  const proxyTarget = theDomain;
  const replaceHost = (uri, appName) => (uri.includes("portal") && uri.replace("portal", appName + '.' + theDomain)) || uri;
  if (!env.port) {
    env.devPort = PORT;
  }


  const devServer = {
    static: [{
      directory: path.resolve(__dirname, 'dist'),
      publicPath: '/',
    }],
    compress: true,
    server: env.DOMAIN.includes("https") ? "https" : "http",
    port: Number(env.devPort),
    allowedHosts: "all",
    historyApiFallback: {
      rewrites: [
        { from: /^\/search\.php$/, to: '/' }
      ]
    },
    proxy: {
      '/api/': {
        target: replaceHost( proxyTarget, 'portal'),
        secure: false,
        changeOrigin: true,
        cookieDomainRewrite: {  "localhost": "areg" },
        withCredentials: true,
      },
      '/proxy/accounts-api/': {
        target: env.ACCOUNTS_API_DOMAIN ? (env.ACCOUNTS_API_DOMAIN) : replaceHost(proxyTarget, 'api.accounts'),
        secure: false,
        changeOrigin: true,
        cookieDomainRewrite: {  "localhost": "areg" },
        withCredentials: true,
        pathRewrite: { '^/proxy/accounts-api': '' }
      },
      '/media/': {
        target: replaceHost(proxyTarget, 'portal'),
        secure: false,
        changeOrigin: true,
        cookieDomainRewrite: { "localhost": "areg" },
        withCredentials: true,
      },
    },
  };

  return merge(
    common(env),
    {
      mode: 'development',
      devtool: 'source-map',
      devServer,
    } 
  )
};
