var amqp = require("amqplib/callback_api");

amqp.connect("amqp://localhost:5672", function (err, conn) {
  conn.createChannel(function (err, ch) {
    var q = "hello";

    ch.assertQueue(q, { durable: true });
    ch.prefetch(1);
    console.log(" [*] Waiting for messages in %s. To exit press CTRL+C", q);
    ch.consume(
      q,
      function (msg) {
        console.info(msg.content.toString());
      },
      { noAck: true }
    );
  });
});
