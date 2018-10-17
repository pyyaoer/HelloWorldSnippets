CPPFLAGS=-lboost_system -lboost_thread -lpthread

client:

.PHONY:
run:
	python server.py &
	./client
clean:
	rm -f *.o client
