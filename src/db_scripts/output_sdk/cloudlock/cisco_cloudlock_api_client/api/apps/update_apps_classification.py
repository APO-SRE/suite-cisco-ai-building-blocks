from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apps_collection import AppsCollection
from ...models.update_apps_classification_body import UpdateAppsClassificationBody
from ...models.update_apps_classification_response_400 import UpdateAppsClassificationResponse400
from ...models.update_apps_classification_response_401 import UpdateAppsClassificationResponse401
from ...models.update_apps_classification_response_403 import UpdateAppsClassificationResponse403
from ...models.update_apps_classification_response_404 import UpdateAppsClassificationResponse404
from ...models.update_apps_classification_response_500 import UpdateAppsClassificationResponse500
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    body: UpdateAppsClassificationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/apps/{id}/classification",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[
        UpdateAppsClassificationResponse400,
        UpdateAppsClassificationResponse401,
        UpdateAppsClassificationResponse403,
        UpdateAppsClassificationResponse404,
        UpdateAppsClassificationResponse500,
        list["AppsCollection"],
    ]
]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AppsCollection.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == 400:
        response_400 = UpdateAppsClassificationResponse400.from_dict(response.json())

        return response_400
    if response.status_code == 401:
        response_401 = UpdateAppsClassificationResponse401.from_dict(response.json())

        return response_401
    if response.status_code == 403:
        response_403 = UpdateAppsClassificationResponse403.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = UpdateAppsClassificationResponse404.from_dict(response.json())

        return response_404
    if response.status_code == 500:
        response_500 = UpdateAppsClassificationResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[
        UpdateAppsClassificationResponse400,
        UpdateAppsClassificationResponse401,
        UpdateAppsClassificationResponse403,
        UpdateAppsClassificationResponse404,
        UpdateAppsClassificationResponse500,
        list["AppsCollection"],
    ]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAppsClassificationBody,
) -> Response[
    Union[
        UpdateAppsClassificationResponse400,
        UpdateAppsClassificationResponse401,
        UpdateAppsClassificationResponse403,
        UpdateAppsClassificationResponse404,
        UpdateAppsClassificationResponse500,
        list["AppsCollection"],
    ]
]:
    """Update Classification for Application

     Update the application's classification.

    Args:
        id (str):
        body (UpdateAppsClassificationBody):  Example: {'other_reason': 'Other Custom Reason',
            'reason_id': 4, 'type': 'trusted'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateAppsClassificationResponse400, UpdateAppsClassificationResponse401, UpdateAppsClassificationResponse403, UpdateAppsClassificationResponse404, UpdateAppsClassificationResponse500, list['AppsCollection']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAppsClassificationBody,
) -> Optional[
    Union[
        UpdateAppsClassificationResponse400,
        UpdateAppsClassificationResponse401,
        UpdateAppsClassificationResponse403,
        UpdateAppsClassificationResponse404,
        UpdateAppsClassificationResponse500,
        list["AppsCollection"],
    ]
]:
    """Update Classification for Application

     Update the application's classification.

    Args:
        id (str):
        body (UpdateAppsClassificationBody):  Example: {'other_reason': 'Other Custom Reason',
            'reason_id': 4, 'type': 'trusted'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateAppsClassificationResponse400, UpdateAppsClassificationResponse401, UpdateAppsClassificationResponse403, UpdateAppsClassificationResponse404, UpdateAppsClassificationResponse500, list['AppsCollection']]
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAppsClassificationBody,
) -> Response[
    Union[
        UpdateAppsClassificationResponse400,
        UpdateAppsClassificationResponse401,
        UpdateAppsClassificationResponse403,
        UpdateAppsClassificationResponse404,
        UpdateAppsClassificationResponse500,
        list["AppsCollection"],
    ]
]:
    """Update Classification for Application

     Update the application's classification.

    Args:
        id (str):
        body (UpdateAppsClassificationBody):  Example: {'other_reason': 'Other Custom Reason',
            'reason_id': 4, 'type': 'trusted'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[UpdateAppsClassificationResponse400, UpdateAppsClassificationResponse401, UpdateAppsClassificationResponse403, UpdateAppsClassificationResponse404, UpdateAppsClassificationResponse500, list['AppsCollection']]]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateAppsClassificationBody,
) -> Optional[
    Union[
        UpdateAppsClassificationResponse400,
        UpdateAppsClassificationResponse401,
        UpdateAppsClassificationResponse403,
        UpdateAppsClassificationResponse404,
        UpdateAppsClassificationResponse500,
        list["AppsCollection"],
    ]
]:
    """Update Classification for Application

     Update the application's classification.

    Args:
        id (str):
        body (UpdateAppsClassificationBody):  Example: {'other_reason': 'Other Custom Reason',
            'reason_id': 4, 'type': 'trusted'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[UpdateAppsClassificationResponse400, UpdateAppsClassificationResponse401, UpdateAppsClassificationResponse403, UpdateAppsClassificationResponse404, UpdateAppsClassificationResponse500, list['AppsCollection']]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
