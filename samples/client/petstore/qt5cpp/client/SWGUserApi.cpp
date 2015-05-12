#include "SWGUserApi.h"
#include "SWGHelpers.h"

#include <QJsonArray>
#include <QJsonDocument>

namespace Swagger {
SWGUserApi::SWGUserApi() {}

SWGUserApi::~SWGUserApi() {}

SWGUserApi::SWGUserApi(QString host, QString basePath) {
    this->host = host;
    this->basePath = basePath;
}

void
SWGUserApi::createUser(SWGUser body) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user");

    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "POST");

    
    // body
    input.request_body.append(body.asJson());
    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::createUserCallback);

    worker->execute(&input);
}

void
SWGUserApi::createUserCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: 

    

    worker->deleteLater();

    
    emit createUserSignal();
}
void
SWGUserApi::createUsersWithArrayInput(QList&lt;SWGUser*&gt;* body) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/createWithArray");

    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "POST");

    
    // body
    input.request_body.append(body.asJson());
    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::createUsersWithArrayInputCallback);

    worker->execute(&input);
}

void
SWGUserApi::createUsersWithArrayInputCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: 

    

    worker->deleteLater();

    
    emit createUsersWithArrayInputSignal();
}
void
SWGUserApi::createUsersWithListInput(QList&lt;SWGUser*&gt;* body) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/createWithList");

    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "POST");

    
    // body
    input.request_body.append(body.asJson());
    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::createUsersWithListInputCallback);

    worker->execute(&input);
}

void
SWGUserApi::createUsersWithListInputCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: 

    

    worker->deleteLater();

    
    emit createUsersWithListInputSignal();
}
void
SWGUserApi::loginUser(QString* username, QString* password) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/login");

    

    if(fullPath.compare("?") > 0) fullPath.append("?");
    else fullPath.append("&");
    fullPath.append(QUrl::toPercentEncoding("username"))
        .append("=")
        .append(QUrl::toPercentEncoding(stringValue(username)));
    if(fullPath.compare("?") > 0) fullPath.append("?");
    else fullPath.append("&");
    fullPath.append(QUrl::toPercentEncoding("password"))
        .append("=")
        .append(QUrl::toPercentEncoding(stringValue(password)));
    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "GET");

    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::loginUserCallback);

    worker->execute(&input);
}

void
SWGUserApi::loginUserCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: QString*

    
    

    
    QString json(worker->response);
    QString* output = new QString(&json);

    
    

    worker->deleteLater();

    emit loginUserSignal(output);
    
}
void
SWGUserApi::logoutUser() {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/logout");

    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "GET");

    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::logoutUserCallback);

    worker->execute(&input);
}

void
SWGUserApi::logoutUserCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: 

    

    worker->deleteLater();

    
    emit logoutUserSignal();
}
void
SWGUserApi::getUserByName(QString* username) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/{username}");

    
    QString usernamePathParam("{"); usernamePathParam.append("username").append("}");
    fullPath.replace(usernamePathParam, stringValue(username));
    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "GET");

    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::getUserByNameCallback);

    worker->execute(&input);
}

void
SWGUserApi::getUserByNameCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: SWGUser*

    
    

    
    QString json(worker->response);
    SWGUser* output = new SWGUser(&json);

    
    

    worker->deleteLater();

    emit getUserByNameSignal(output);
    
}
void
SWGUserApi::updateUser(QString* username, SWGUser body) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/{username}");

    
    QString usernamePathParam("{"); usernamePathParam.append("username").append("}");
    fullPath.replace(usernamePathParam, stringValue(username));
    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "PUT");

    
    // body
    input.request_body.append(body.asJson());
    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::updateUserCallback);

    worker->execute(&input);
}

void
SWGUserApi::updateUserCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: 

    

    worker->deleteLater();

    
    emit updateUserSignal();
}
void
SWGUserApi::deleteUser(QString* username) {
    QString fullPath;
    fullPath.append(this->host).append(this->basePath).append("/user/{username}");

    
    QString usernamePathParam("{"); usernamePathParam.append("username").append("}");
    fullPath.replace(usernamePathParam, stringValue(username));
    

    

    // qDebug() << fullPath;

    HttpRequestWorker *worker = new HttpRequestWorker();
    HttpRequestInput input(fullPath, "DELETE");

    

    

    connect(worker,
            &HttpRequestWorker::on_execution_finished,
            this,
            &SWGUserApi::deleteUserCallback);

    worker->execute(&input);
}

void
SWGUserApi::deleteUserCallback(HttpRequestWorker * worker) {
    QString msg;
    if (worker->error_type == QNetworkReply::NoError) {
        msg = QString("Success! %1 bytes").arg(worker->response.length());
    }
    else {
        msg = "Error: " + worker->error_str;
    }

    // return type: 

    

    worker->deleteLater();

    
    emit deleteUserSignal();
}
} /* namespace Swagger */
