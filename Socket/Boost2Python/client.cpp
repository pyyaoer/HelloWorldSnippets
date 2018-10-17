#include <boost/asio.hpp>
#include <chrono>
#include <thread>
#include <iostream>

static const int PORT = 52275;

int main(void) {
  // wait 0.5s for the server 
  std::this_thread::sleep_for(std::chrono::milliseconds(500));
  boost::asio::io_service io_service;
  boost::asio::ip::tcp::socket socket(io_service);
  boost::asio::ip::tcp::resolver resolver(io_service);
  boost::asio::ip::tcp::resolver::iterator endpoint = 
    resolver.resolve(boost::asio::ip::tcp::resolver::query("127.0.0.1", std::to_string(PORT)));
  boost::asio::connect(socket, endpoint);
  socket.send(boost::asio::buffer("Hello world!"));
}
