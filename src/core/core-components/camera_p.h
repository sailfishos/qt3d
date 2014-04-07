/****************************************************************************
**
** Copyright (C) 2014 Klaralvdalens Datakonsult AB (KDAB).
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

#ifndef CAMERA_P_H
#define CAMERA_P_H

#include <QMatrix4x4>
#include <QVector3D>

#include <Qt3DCore/cameralens.h>
#include <Qt3DCore/lookattransform.h>
#include <Qt3DCore/transform.h>

QT_BEGIN_NAMESPACE

namespace Qt3D {

class CameraPrivate
{
public:
    CameraPrivate(Camera *qq)
        : q_ptr(qq),
          m_lens(new CameraLens()),
          m_lookAt(new LookAtTransform()),
          m_transform(new Transform())
    {
        m_transform->appendTransfrom(m_lookAt);
        qq->addComponent(m_transform);
        qq->addComponent(m_lens);
    }

    Q_DECLARE_PUBLIC(Camera)
    Camera *q_ptr;

    CameraLens *m_lens;
    LookAtTransform *m_lookAt;
    Transform *m_transform;
};

} // namespace Qt3D

QT_END_NAMESPACE

#endif // CAMERA_P_H