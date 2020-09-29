MVC 패턴

Model : DTO (data transfer object) + DAO (data access object)
Service: Business Login (Algorithm)
Controller: RESTful 방식으로 React Axios로 통신

MVC 패턴

모델 (model) - 핵심 기능과 데이터를 포함
             - Service, Model
                        - DTO, DAO
             - Model (.py = memory) : Machine (*.h5 = hardisk) 저장된 형태

뷰 (view) - 사용자에게 정보를 표시 (하나 이상의 뷰가 정의될 수 있음)
컨트롤러(controller) - UI로부터 입출력을 처리
