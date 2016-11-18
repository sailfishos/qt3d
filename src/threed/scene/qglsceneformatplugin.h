/****************************************************************************
**
** Copyright (C) 2012 Digia Plc and/or its subsidiary(-ies).
** Contact: http://www.qt-project.org/legal
**
** This file is part of the Qt3D module of the Qt Toolkit.
**
** $QT_BEGIN_LICENSE:LGPL$
** Commercial License Usage
** Licensees holding valid commercial Qt licenses may use this file in
** accordance with the commercial license agreement provided with the
** Software or, alternatively, in accordance with the terms contained in
** a written agreement between you and Digia.  For licensing terms and
** conditions see http://qt.digia.com/licensing.  For further information
** use the contact form at http://qt.digia.com/contact-us.
**
** GNU Lesser General Public License Usage
** Alternatively, this file may be used under the terms of the GNU Lesser
** General Public License version 2.1 as published by the Free Software
** Foundation and appearing in the file LICENSE.LGPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU Lesser General Public License version 2.1 requirements
** will be met: http://www.gnu.org/licenses/old-licenses/lgpl-2.1.html.
**
** In addition, as a special exception, Digia gives you certain additional
** rights.  These rights are described in the Digia Qt LGPL Exception
** version 1.1, included in the file LGPL_EXCEPTION.txt in this package.
**
** GNU General Public License Usage
** Alternatively, this file may be used under the terms of the GNU
** General Public License version 3.0 as published by the Free Software
** Foundation and appearing in the file LICENSE.GPL included in the
** packaging of this file.  Please review the following information to
** ensure the GNU General Public License version 3.0 requirements will be
** met: http://www.gnu.org/copyleft/gpl.html.
**
**
** $QT_END_LICENSE$
**
****************************************************************************/

#ifndef QGLSCENEFORMATPLUGIN_H
#define QGLSCENEFORMATPLUGIN_H

#include <Qt3D/qt3dglobal.h>
#include <QtCore/qplugin.h>
#include <QtCore/qfactoryinterface.h>
#include <QtCore/qurl.h>
#include <QObject>
#include <QIODevice>

QT_BEGIN_NAMESPACE

class QGLAbstractScene;
class QGLSceneFormatHandlerPrivate;
class QDownloadManager;

class Q_QT3D_EXPORT QGLSceneFormatHandler : public QObject
{
    Q_OBJECT
public:
    QGLSceneFormatHandler();
    virtual ~QGLSceneFormatHandler();

    QIODevice *device() const;
    void setDevice(QIODevice *device);

    QString format() const;
    void setFormat(const QString& format);

    QUrl url() const;
    void setUrl(const QUrl& url);

    virtual QGLAbstractScene *read() = 0;
    virtual QGLAbstractScene *download() = 0;

    virtual void decodeOptions(const QString &options);

    void finalize();
    void downloadScene();

public Q_SLOTS:
    virtual void downloadComplete(QByteArray *sceneData);

protected:
    void setScene(QGLAbstractScene *theScene);
    QGLAbstractScene * getScene() const;

    QDownloadManager *m_downloadManager;
private:
    QGLSceneFormatHandlerPrivate *d_ptr;
};

class Q_QT3D_EXPORT QGLSceneFormatFactoryInterface
{
public:
    virtual ~QGLSceneFormatFactoryInterface() {}
    virtual QGLSceneFormatHandler *create(QIODevice *device, const QUrl& url, const QString &format = QString()) const = 0;
};

Q_DECLARE_INTERFACE(QGLSceneFormatFactoryInterface, "org.qt-project.Qt.QGLSceneFormatFactoryInterface")

QT_END_NAMESPACE

#endif
