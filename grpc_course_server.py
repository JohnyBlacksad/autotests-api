import grpc
from concurrent import futures
import course_service_pb2
import course_service_pb2_grpc

class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    def GetCourse(self, request, context):
        title = 'Автотесты API'
        description = 'Будем изучать автотесты API'
        return course_service_pb2.GetCourseResponse(course_id=request.course_id,
                                                    title=title,
                                                    description=description)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Course сервер запущен')
    server.wait_for_termination()
    
if __name__ == '__main__':
    serve()