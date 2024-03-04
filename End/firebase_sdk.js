const admin = require("firebase-admin");

const serviceAccount = require("./serviceAccountKey.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://sunnypedia-g13-default-rtdb.firebaseio.com"
});

const db = admin.database();
const ref = db.ref("some/path"); // 替换 "some/path" 为您想要存储数据的路径

// 定义示例数据
const exampleData = {
    name: "John Doe",
    age: 30,
    hasAccess: true
};

// 将数据推送到指定的路径
ref.set(exampleData, function(error) {
    if (error) {
      console.log("Data could not be saved." + error);
    } else {
      console.log("Data saved successfully.");
      // 关闭应用实例
      admin.app().delete().then(() => {
        console.log('Firebase connection closed.');
      });
    }
  });