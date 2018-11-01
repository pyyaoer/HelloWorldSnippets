#include <boost/thread.hpp>

void do_sth() {
  boost::this_thread::sleep_for(boost::chrono::milliseconds(100));
  std::cout << "do_sth" << std::endl;
}

void do_sth_with_args(int arg) {
  boost::this_thread::sleep_for(boost::chrono::milliseconds(100));
  std::cout << arg << std::endl;
}

void do_sth_timeout() {
  boost::this_thread::sleep_for(boost::chrono::milliseconds(100));
  std::cout << "Not timeout" << std::endl;
}

int main(void) {
  // one thread
  boost::thread t1{do_sth};
  t1.join();
  boost::thread t2(do_sth);
  t2.join();

  // thread with an argument
  boost::thread ta1{do_sth_with_args, 1};
  ta1.join();
  boost::thread ta2{do_sth_with_args, 2};
  ta2.join();

  // a thread group
  boost::thread_group tg;
  tg.create_thread(do_sth);
  tg.create_thread(boost::bind(do_sth_with_args, 3));
  tg.join_all();

  // threads with timeout
  boost::thread to1{do_sth_timeout};
  if (!to1.try_join_for(boost::chrono::milliseconds(90))) {
    std::cout << "Timeout!" << std::endl;
  }
  boost::thread to2{do_sth_timeout};
  if (!to1.try_join_for(boost::chrono::seconds(110))) {
    std::cout << "Timeout!" << std::endl;
  }

  // a thread with return value
  int ret = 0;
  boost::thread tr([&ret] {ret = 1;});
  tr.join();
  std::cout << ret << std::endl;

  return 0;

}
